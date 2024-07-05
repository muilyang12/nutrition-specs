"use client";

import { useEffect } from "react";
import { useComparingProductsStore } from "@stores/comparingProductsStore";
import { useUrlSearchParams } from "@hooks/useUrlSearchParams";
import { foodApi } from "@apis/food";
import { ProductNutritionResult } from "@apis/food.define";

export default function ComparingTargets() {
  const { getQueryParams, deleteQueryParams } = useUrlSearchParams();

  const { setComparingProducts } = useComparingProductsStore();

  useEffect(() => {
    const productIds = getQueryParams("product");

    Promise.all(
      productIds.map((id) => {
        const idNum = Number(id);

        if (Number.isInteger(idNum)) {
          return foodApi.getProductNutrition(idNum);
        } else {
          deleteQueryParams([{ key: "product", value: id }]);
          return;
        }
      })
    ).then((result) => {
      const newProductNutritions: Record<string, ProductNutritionResult> = {};

      result.forEach((data, index) => {
        if (!data) return;

        newProductNutritions[productIds[index]] = data;
      });

      setComparingProducts(newProductNutritions);
    });
  }, []);

  return <></>;
}
