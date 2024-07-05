"use client";

import { useEffect } from "react";
import { useComparingProductsStore } from "@stores/comparingProductsStore";
import { useUrlSearchParams } from "@hooks/useUrlSearchParams";
import { foodApi } from "@apis/food";
import { ProductNutritionResult } from "@apis/food.define";
import styles from "./ComparingTargets.module.css";

export default function ComparingTargets() {
  const { getQueryParams, deleteQueryParams } = useUrlSearchParams();

  const { comparingProducts, setComparingProducts } = useComparingProductsStore();

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

  return (
    <>
      <div className={styles.comparingTargetsWrapper}>
        <span className={styles.comparingTitle}>Products</span>
        <div className={styles.comparingItems}>
          {Object.values(comparingProducts).map((product, index) => {
            return (
              <div className={styles.comparingItem}>
                <div className={styles.comparingItemLeft}>
                  <span>{index + 1}</span>
                </div>
                <div className={styles.comparingItemRight}>
                  <span>{product.product_name}</span>
                  <span>{product.brand_name}</span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
}
