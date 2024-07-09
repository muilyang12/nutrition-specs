"use client";

import { useRouter } from "next/navigation";
import { FoodCategoryRs } from "@apis/food.define";
import styles from "./CategoryMenu.module.css";

interface Props {
  selectedFoodCategoryKey?: string;
  mainCategories: FoodCategoryRs[];
}

export default function CategoryMenu(props: Props) {
  const { selectedFoodCategoryKey, mainCategories } = props;

  const router = useRouter();

  const handleClickMenuItem = (categoryKey: string) => () => {
    router.push(`/${categoryKey}`);
  };

  return (
    <div className={styles.categoryMenuWrapper}>
      {mainCategories.map((category) => (
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
