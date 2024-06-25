import { NutritionRs } from "@apis/food.define";
import { NUTRITION_KEY_NAME_MAPPER } from "@defines/nutrition";
import styles from "./ProductDetail.module.css";

interface Props {
  nutrition: NutritionRs;
}

export default function ProductDetail(props: Props) {
  const { nutrition } = props;

  const servingExplanation = nutrition.data.serving_size + nutrition.data.serving_unit;

  return (
    <>
      <span>{servingExplanation} 당</span>
      <div className={styles.nutritionalFacts}>
        {Object.entries(nutrition.data).map(([key, value]) => {
          if (key == "serving_size" || key == "serving_unit") return;

          return (
            <div key={`${nutrition.id}-${key}`}>
              {NUTRITION_KEY_NAME_MAPPER[key as keyof typeof NUTRITION_KEY_NAME_MAPPER]}: {value}
            </div>
          );
        })}
      </div>

      <img src={nutrition.s3_url} />
    </>
  );
}
