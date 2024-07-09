"use client";

import { useEffect } from "react";
import { useComparingProductsStore } from "@stores/comparingProductsStore";
import { useUrlSearchParams } from "@hooks/useUrlSearchParams";
import { foodApi } from "@apis/food";
import { ProductNutritionResult } from "@apis/food.define";
import LoadingSpinner from "@components/loading-spinner/LoadingSpinner";
import styles from "./ComparingTargets.module.css";

export default function ComparingTargets() {
  const { getQueryParams, deleteQueryParams } = useUrlSearchParams();

  const { comparingProducts, setComparingProducts } = useComparingProductsStore();
  const productNutritions = Object.values(comparingProducts);

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
        <LoadingSpinner isLoadingDone={productNutritions.length > 0}>
          <div className={styles.comparingItems}>
            {productNutritions.map((product, index) => {
              return (
                <div className={styles.comparingItem} key={`target-product-${product.id}`}>
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
        </LoadingSpinner>
      </div>
    </>
  );
}
