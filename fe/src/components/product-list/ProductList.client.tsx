"use client";

import { useEffect, useRef, useState } from "react";
import { useBrandFilterStore } from "@stores/brandFilterStore";
import ProductCard from "@components/product-card/ProductCard";
import { foodApi } from "@apis/food";
import { ProductNutritionResult } from "@apis/food.define";
import styles from "./ProductList.module.css";

interface Props {
  selectedFoodCategoryKey: string;
  initialProductsNutritions: ProductNutritionResult[];
}

export default function ProductList(props: Props) {
  const { selectedFoodCategoryKey, initialProductsNutritions } = props;

  const [productsAndNutritions, setProductsAndNutritions] = useState(initialProductsNutritions);

  const { selectedFilters } = useBrandFilterStore();

  const apiTriggerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    foodApi.getProductNutritions(selectedFoodCategoryKey, selectedFilters).then((data) => {
      setProductsAndNutritions(data.results);
    });
  }, [selectedFilters]);

  useEffect(() => {
    if (!apiTriggerRef.current) return;

    const intersectionObserver = new IntersectionObserver(function (entries) {
      if (entries[0].intersectionRatio <= 0) return;

      console.log("Load new data.");
    });

    intersectionObserver.observe(apiTriggerRef.current);
  }, []);

  return (
    <>
      <div className={styles.productListWrapper}>
        {productsAndNutritions?.map((productNutrition) => (
          <ProductCard productNutrition={productNutrition} key={productNutrition.id} />
        ))}
      </div>
      <div ref={apiTriggerRef} className={styles.apiTrigger} />
    </>
  );
}
