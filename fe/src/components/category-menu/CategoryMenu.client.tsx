"use client";

import { useRouter } from "next/navigation";
import { FoodCategoryRs } from "@apis/food.define";
import styles from "./CategoryMenu.module.css";

interface Props {
  selectedFoodCategoryKey?: string;
  categories: FoodCategoryRs[];
}

export default function CategoryMenu(props: Props) {
  const { selectedFoodCategoryKey, categories } = props;

  const router = useRouter();

  const handleClickMenuItem = (categoryKey: string) => () => {
    router.push(`/${categoryKey}`);
  };

  return (
    <div className={styles.categoryMenuWrapper}>
      {categories.map((category) => (
        <div
          className={`${styles.categoryMenuItem} ${
            selectedFoodCategoryKey == category.category_key && styles.selectedCategoryMenuItem
          }`}
          onClick={handleClickMenuItem(category.category_key)}
          key={category.id}
        >
          {category.category_name}
        </div>
      ))}
    </div>
  );
}
