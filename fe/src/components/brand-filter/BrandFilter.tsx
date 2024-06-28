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

  return (
    <div className={styles.brandFilterWraper}>
      {brands.map((brand) => (
        <div className={styles.brandFilter} key={brand.id}>
          {brand.name}
        </div>
      ))}
    </div>
  );
}
