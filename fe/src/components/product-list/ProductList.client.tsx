"use client";

import { useEffect, useRef, useState } from "react";
import { useBrandFilterStore } from "@stores/brandFilterStore";
import ProductCard from "@components/product-card/ProductCard";
import { foodApi } from "@apis/food";
import { ProductDetailResult } from "@apis/food.define";
import styles from "./ProductList.module.css";

interface Props {
  selectedFoodCategoryKey: string;
  initialProductsNutritions: ProductDetailResult[];
  maxPage: number;
}

export default function ProductList(props: Props) {
  const { selectedFoodCategoryKey, initialProductsNutritions, maxPage } = props;

  const [productsAndNutritions, setProductsAndNutritions] = useState(initialProductsNutritions);

  const { selectedFilters } = useBrandFilterStore();

  const apiTriggerRef = useRef<HTMLDivElement>(null);
  const currentPageRef = useRef<number>(1);
  const [isAbleToLoadNext, setIsAbleToLoadNext] = useState(maxPage > 1);

  useEffect(() => {
    if (selectedFilters.length === 0) return;

    foodApi.getProductDetails(selectedFoodCategoryKey, selectedFilters).then((data) => {
      setProductsAndNutritions(data.results);
    });
    currentPageRef.current = 1;
  }, [selectedFilters]);

  useEffect(() => {
    if (!apiTriggerRef.current) return;

    const intersectionObserver = new IntersectionObserver((entries) => {
      if (entries[0].intersectionRatio <= 0) return;

      currentPageRef.current += 1;

      if (currentPageRef.current > maxPage) {
        setIsAbleToLoadNext(false);
        intersectionObserver.disconnect();

        return;
      }

      foodApi
        .getProductDetails(selectedFoodCategoryKey, selectedFilters, currentPageRef.current)
        .then((data) => {
          setProductsAndNutritions((prev) => [...prev, ...data.results]);
        })
        .catch(() => intersectionObserver.disconnect());
    });

    intersectionObserver.observe(apiTriggerRef.current);
  }, [selectedFilters]);

  return (
    <>
      <div className={styles.productListWrapper}>
        {productsAndNutritions?.map((productNutrition) => (
          <ProductCard productNutrition={productNutrition} key={productNutrition.id} />
        ))}
      </div>
      {isAbleToLoadNext && <div ref={apiTriggerRef} className={styles.apiTrigger} />}
    </>
  );
}
