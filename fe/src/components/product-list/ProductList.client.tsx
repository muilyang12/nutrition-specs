"use client";

import { useEffect, useState } from "react";
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

  useEffect(() => {
    foodApi.getProductNutritions(selectedFoodCategoryKey, selectedFilters).then((data) => {
      setProductsAndNutritions(data.results);
    });
  }, [selectedFilters]);

  return (
    <div className={styles.productListWrapper}>
      {productsAndNutritions?.map((productNutrition) => (
        <ProductCard productNutrition={productNutrition} key={productNutrition.id} />
      ))}
    </div>
  );
}
