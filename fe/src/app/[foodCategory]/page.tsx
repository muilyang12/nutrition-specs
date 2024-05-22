import FoodCategoryView from "@views/FoodCategoryView";
import { foodApi } from "@apis/food";

interface PathParams {
  params: {
    foodCategory: string;
  };
}

export default async function FoodCategoryPage({ params }: PathParams) {
  return (
    <>
      <FoodCategoryView />
    </>
  );
}

export async function generateStaticParams() {
  const foodCategories = await foodApi.getFoodCategories();

  return foodCategories.map((category) => ({
    foodCategory: category.category_key,
  }));
}
