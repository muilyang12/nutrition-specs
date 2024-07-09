"use client";

import { useEffect } from "react";
import classNames from "classnames";
import { useUrlSearchParams } from "@hooks/useUrlSearchParams";
import { useBrandFilterStore } from "@stores/brandFilterStore";
import { BrandRs } from "@apis/food.define";
import styles from "./BrandFilter.module.css";

interface Props {
  brands: BrandRs[];
}

export default function BrandFilter(props: Props) {
  const { brands } = props;

  const { getQueryParams, appendQueryParams, deleteQueryParams } = useUrlSearchParams();

  const { selectedFilters, setSelectedFilters, addSelectedFilter, deleteSelectedFilter } =
    useBrandFilterStore();
  useEffect(() => {
    const brands = getQueryParams("brand");
    if (brands.length === 0) return;

    setSelectedFilters(brands);
  }, []);

  const handleBrandClick = (brand: BrandRs) => {
    const isSelected = selectedFilters.includes(brand.name);

    if (isSelected) {
      deleteQueryParams([{ key: "brand", value: brand.name }]);
      deleteSelectedFilter(brand.name);
    } else {
      appendQueryParams({ brand: brand.name });
      addSelectedFilter(brand.name);
    }
  };

  return (
    <div className={styles.brandFilterWraper}>
      {brands.map((brand) => (
        <div
          className={classNames(
            styles.brandFilter,
            selectedFilters.includes(brand.name) && styles.selectedBrandFilter
          )}
          onClick={() => handleBrandClick(brand)}
          key={brand.id}
        >
          {brand.name}
        </div>
      ))}
    </div>
  );
}
