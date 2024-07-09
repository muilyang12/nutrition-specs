"use client";

import { useRouter } from "next/navigation";
import classNames from "classnames";
import { FoodCategoryRs } from "@apis/food.define";
import styles from "./MainCategoryMenu.module.css";

interface Props {
  selectedMainCategoryKey?: string;
  mainCategories: FoodCategoryRs[];
}

export default function MainCategoryMenu(props: Props) {
  const { selectedMainCategoryKey, mainCategories } = props;

  const router = useRouter();

  const handleClickMenuItem = (categoryKey: string) => () => {
    router.push(`/${categoryKey}`);
  };

  return (
    <div className={styles.mainCategoryMenuWrapper}>
      {mainCategories.map((category) => (
        <div
          className={classNames(
            styles.mainCategoryMenuItem,
            selectedMainCategoryKey == category.category_key && styles.selectedMainCategoryMenuItem
          )}
          onClick={handleClickMenuItem(category.category_key)}
          key={category.id}
        >
          {category.category_name}
        </div>
      ))}
    </div>
  );
}
