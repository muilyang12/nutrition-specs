"use client";

import { NUTRITION_KEY_NAME_MAPPER } from "@defines/nutrition";
import { useComparingProductsStore } from "@stores/comparingProductsStore";
import styles from "./ComparingDataMainTable.module.css";

export default function ComparingDataMainTable() {
  const { comparingProducts } = useComparingProductsStore();

  return (
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
        {Object.values(comparingProducts).map((product, index) => {
          const nutrition = product.nutritions[0];

          return (
            <tr key={`main-tbody-row-${product.id}`}>
              <td className={styles.tableIndexCol}>{index + 1}</td>
              <td>{`${nutrition.data.calories} kcal`}</td>
              <td>{`${nutrition.data.total_carbohydrate}g`}</td>
              <td>{`${nutrition.data.sugars}g`}</td>
              <td>{`${nutrition.data.total_fat}g`}</td>
              <td>{`${nutrition.data.protein}g`}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}
