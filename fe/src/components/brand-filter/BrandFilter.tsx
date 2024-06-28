"use client";

import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { FoodCategoryPageParams } from "@defines/params.define";
import { useUrlSearchParams } from "@hooks/useUrlSearchParams";
import { foodApi } from "@apis/food";
import { BrandRs } from "@apis/food.define";
import styles from "./BrandFilter.module.css";

export default function BrandFilter() {
  const params = useParams<FoodCategoryPageParams>();
  const selectedFoodCategoryKey = params.foodCategory;
  const { appendQueryParams, deleteQueryParams } = useUrlSearchParams();

  const [brands, setBrands] = useState<BrandRs[]>([]);
  useEffect(() => {
    foodApi.getBrands(selectedFoodCategoryKey).then((brands) => setBrands(brands));
  }, []);

  const [selectedFilters, setSelectedFilters] = useState<number[]>([]);
  const handleBrandClick = (brand: BrandRs) => {
    const isSelected = selectedFilters.includes(brand.id);

    if (isSelected) deleteQueryParams([{ key: "brand", value: brand.name }]);
    else appendQueryParams({ brand: brand.name });

    setSelectedFilters((prevFilters) =>
      isSelected ? prevFilters.filter((id) => id !== brand.id) : [...prevFilters, brand.id]
    );
  };

  return (
    <div className={styles.brandFilterWraper}>
      {brands.map((brand) => (
        <div
          className={`${styles.brandFilter} ${
            selectedFilters.includes(brand.id) ? styles.selectedBrandFilter : ""
          }`}
          onClick={() => handleBrandClick(brand)}
          key={brand.id}
        >
          {brand.name}
        </div>
      ))}
    </div>
  );
}
