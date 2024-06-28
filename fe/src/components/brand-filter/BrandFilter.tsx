"use client";

import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { FoodCategoryPageParams } from "@defines/params.define";
import { foodApi } from "@apis/food";
import { BrandRs } from "@apis/food.define";
import styles from "./BrandFilter.module.css";

export default function BrandFilter() {
  const params = useParams<FoodCategoryPageParams>();
  const selectedFoodCategoryKey = params.foodCategory;

  const [brands, setBrands] = useState<BrandRs[]>([]);
  useEffect(() => {
    foodApi.getBrands(selectedFoodCategoryKey).then((brands) => setBrands(brands));
  }, []);

  const [selectedFilters, setSelectedFilters] = useState<number[]>([]);
  const handleBrandClick = (brandId: number) => {
    setSelectedFilters((prevFilters) => {
      if (prevFilters.includes(brandId)) {
        return prevFilters.filter((id) => id !== brandId);
      } else {
        return [...prevFilters, brandId];
      }
    });
  };

  return (
    <div className={styles.brandFilterWraper}>
      {brands.map((brand) => (
        <div
          className={`${styles.brandFilter} ${
            selectedFilters.includes(brand.id) ? styles.selectedBrandFilter : ""
          }`}
          onClick={() => handleBrandClick(brand.id)}
          key={brand.id}
        >
          {brand.name}
        </div>
      ))}
    </div>
  );
}
