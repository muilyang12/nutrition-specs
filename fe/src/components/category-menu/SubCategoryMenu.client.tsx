"use client";

import { useRouter } from "next/navigation";
import classNames from "classnames";
import { FoodCategoryRs } from "@apis/food.define";
import styles from "./SubCategoryMenu.module.css";

interface Props {
  subCategories: FoodCategoryRs[];
  selectedSubCategoryKey?: string;
}

export default function SubCategoryMenu(props: Props) {
  const { subCategories, selectedSubCategoryKey } = props;

  const router = useRouter();

  const handleBrandClick = (newSubCategory: FoodCategoryRs) => {
    router.push(`./${newSubCategory.category_key}`);
  };

  return (
    <div className={styles.subCategoryWraper}>
      {subCategories.map((category) => (
        <div
          className={classNames(
            styles.subCategory,
            category.category_key === selectedSubCategoryKey && styles.selectedSubCategory
          )}
          onClick={() => handleBrandClick(category)}
          key={category.id}
        >
          {category.category_name}
        </div>
      ))}
    </div>
  );
}
