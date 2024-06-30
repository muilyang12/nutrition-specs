"use client";

import { useState } from "react";
import ProductCard from "@components/product-card/ProductCard";
import { ProductsAndNutritions } from "./ProductList.define";
import styles from "./ProductList.module.css";

interface Props {
  selectedFoodCategoryKey?: string;
  initialProductsAndNutritions: ProductsAndNutritions;
}

export default function ProductList(props: Props) {
  const { selectedFoodCategoryKey, initialProductsAndNutritions } = props;

  const [productsAndNutritions, setProductsAndNutritions] = useState(initialProductsAndNutritions);

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
