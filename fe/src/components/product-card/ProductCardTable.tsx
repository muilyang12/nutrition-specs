import { NUTRITION_KEY_NAME_MAPPER } from "@defines/nutrition";
import { NutritionRs } from "@apis/food.define";
import styles from "./ProductCardTable.module.css";

interface Props {
  nutrition: NutritionRs;
}

export default function ProductCardTable(props: Props) {
  const { nutrition } = props;

  return (
    <table className={styles.table}>
      <tbody>
        <tr>
          <td>{NUTRITION_KEY_NAME_MAPPER["total_carbohydrate"]}</td>
          <td>{`${nutrition.data.total_carbohydrate}g`}</td>
          <td>{NUTRITION_KEY_NAME_MAPPER["sugars"]}</td>
          <td>{`${nutrition.data.sugars}g`}</td>
        </tr>
        <tr>
          <td>{NUTRITION_KEY_NAME_MAPPER["protein"]}</td>
          <td>{`${nutrition.data.protein}g`}</td>
          <td>{NUTRITION_KEY_NAME_MAPPER["total_fat"]}</td>
          <td>{`${nutrition.data.total_fat}g`}</td>
        </tr>
      </tbody>
    </table>
  );
}
