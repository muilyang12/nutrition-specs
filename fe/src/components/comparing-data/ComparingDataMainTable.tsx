"use client";

import { useComparingProductsStore } from "@stores/comparingProductsStore";
import { NUTRITION_KEY_NAME_MAPPER } from "@defines/nutrition";
import { getNutritionWithUnit } from "@utils/nutrition";
import LoadingSpinner from "@components/loading-spinner/LoadingSpinner";
import styles from "./ComparingDataMainTable.module.css";

export default function ComparingDataMainTable() {
  const { comparingProducts } = useComparingProductsStore();

  const productNutritions = Object.values(comparingProducts);

  return (
    <LoadingSpinner isLoadingDone={productNutritions.length > 0}>
      <table className={styles.table}>
        <thead>
          <tr>
            <td className={styles.tableIndexCol}></td>
            <td>{NUTRITION_KEY_NAME_MAPPER["calories"]}</td>
            <td>{NUTRITION_KEY_NAME_MAPPER["total_carbohydrate"]}</td>
            <td>{NUTRITION_KEY_NAME_MAPPER["sugars"]}</td>
            <td>{NUTRITION_KEY_NAME_MAPPER["total_fat"]}</td>
            <td>{NUTRITION_KEY_NAME_MAPPER["protein"]}</td>
          </tr>
        </thead>
        <tbody>
          {productNutritions.map((product, index) => {
            const nutrition = product.nutritions[0];

            return (
              <tr key={`main-tbody-row-${product.id}`}>
                <td className={styles.tableIndexCol}>{index + 1}</td>
                <td>{getNutritionWithUnit("calories", nutrition.data.calories)}</td>
                <td>
                  {getNutritionWithUnit("total_carbohydrate", nutrition.data.total_carbohydrate)}
                </td>
                <td>{getNutritionWithUnit("sugars", nutrition.data.sugars)}</td>
                <td>{getNutritionWithUnit("total_fat", nutrition.data.total_fat)}</td>
                <td>{getNutritionWithUnit("protein", nutrition.data.protein)}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </LoadingSpinner>
  );
}
