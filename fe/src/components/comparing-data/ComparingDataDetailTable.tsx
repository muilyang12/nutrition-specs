"use client";

import { useComparingProductsStore } from "@stores/comparingProductsStore";
import { NUTRITION_KEY_NAME_MAPPER } from "@defines/nutrition";
import { NutritionData } from "@apis/food.define";
import styles from "./ComparingDataDetailTable.module.css";

export default function ComparingDataDetailTable() {
  const { comparingProducts } = useComparingProductsStore();

  const productsValues = Object.values(comparingProducts);

  return (
    <table className={styles.table}>
      <thead>
        <tr>
          <td></td>
          {productsValues.map((product, index) => (
            <td key={`detail-thead-cell-${product.id}`}>{index + 1}</td>
          ))}
        </tr>
      </thead>

      <tbody>
        {Object.entries(NUTRITION_KEY_NAME_MAPPER).map(([key, value]) => {
          return (
            <tr key={`detail-tbody-row-${key}`}>
              <td>{value}</td>
              {productsValues.map((product) => {
                const nutrition = product.nutritions[0];

                return (
                  <td
                    style={{ width: `${67 / productsValues.length}%` }}
                    key={`detail-tbody-cell-${product.id}`}
                  >
                    {nutrition.data[key as keyof NutritionData]}
                  </td>
                );
              })}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}
