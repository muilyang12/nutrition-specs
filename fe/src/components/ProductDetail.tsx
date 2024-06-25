import { NutritionRs } from "@apis/food.define";

interface Props {
  nutrition: NutritionRs;
}

export default function ProductDetail(props: Props) {
  const { nutrition } = props;

  return (
    <>
      {Object.entries(nutrition.data).map(([key, value]) => (
        <div>
          {key}: {value}
        </div>
      ))}

      <img src={nutrition.s3_url} />
    </>
  );
}
