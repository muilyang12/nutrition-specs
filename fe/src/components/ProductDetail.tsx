import { NutritionRs } from "@apis/food.define";
import { NUTRITION_KEY_NAME_MAPPER } from "@defines/nutrition";

interface Props {
  nutrition: NutritionRs;
}

export default function ProductDetail(props: Props) {
  const { nutrition } = props;

  const servingExplanation = nutrition.data.serving_size + nutrition.data.serving_unit;

  return (
    <>
      {servingExplanation} 당
      {Object.entries(nutrition.data).map(([key, value]) => {
        if (key == "serving_size" || key == "serving_unit") return;

        return (
          <div key={nutrition.id}>
            {NUTRITION_KEY_NAME_MAPPER[key as keyof typeof NUTRITION_KEY_NAME_MAPPER]}: {value}
          </div>
        );
      })}
      <img src={nutrition.s3_url} />
    </>
  );
}
