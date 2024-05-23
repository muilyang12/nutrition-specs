import { NutritionRs } from "@apis/food.define";

interface Props {
  nutrition: NutritionRs;
}

export default function ProductDetail(props: Props) {
  const { nutrition } = props;

  return (
    <>
      <div>calory: {nutrition.calory}</div>
      <div>carbohydrate: {nutrition.carbohydrate}</div>
      <div>protein: {nutrition.protein}</div>
      <div>fat: {nutrition.fat}</div>
    </>
  );
}
