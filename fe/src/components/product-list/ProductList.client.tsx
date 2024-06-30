"use client";

import { useEffect, useState } from "react";
import { useBrandFilterStore } from "@stores/brandFilterStore";
import ProductCard from "@components/product-card/ProductCard";
import { foodApi } from "@apis/food";
import { ProductsAndNutritions } from "./ProductList.define";
import styles from "./ProductList.module.css";

interface Props {
  selectedFoodCategoryKey: string;
  initialProductsAndNutritions: ProductsAndNutritions;
}

export default function ProductList(props: Props) {
  const { selectedFoodCategoryKey, initialProductsAndNutritions } = props;

  const [productsAndNutritions, setProductsAndNutritions] = useState(initialProductsAndNutritions);

  const { selectedFilters } = useBrandFilterStore();

  useEffect(() => {
    foodApi.getProducts(selectedFoodCategoryKey, selectedFilters).then((data) => {
      console.log(data.results);
    });
  }, [selectedFilters]);
  return (
    <div className={styles.productListWrapper}>
      {productsAndNutritions.map(([product, nutrition]) => (
        <ProductCard
          product={product}
          nutrition={nutrition}
          key={`${product.id}-${nutrition.id}`}
        />
      ))}
    </div>
  );
}
