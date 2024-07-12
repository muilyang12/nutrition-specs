import FoodCategoryView from "@views/FoodCategoryView";
import { foodApi } from "@apis/food";

interface PathParams {
  params: {
    foodCategory: string;
  };
}

export async function generateMetadata({ params }: PathParams) {
  const foodCategory = await foodApi.getFoodCategoryByCategoryKey(params.foodCategory);

  return {
    title: `Nutrition Specs - Comparing ${foodCategory.category_name}`,
  };
}

export default async function FoodCategoryPage({ params }: PathParams) {
  return (
    <>
      <FoodCategoryView selectedFoodCategoryKey={params.foodCategory} />
    </>
  );
}

export async function generateStaticParams() {
  const foodCategories = await foodApi.getAllFoodCategories();

  return foodCategories.map((category) => ({
    foodCategory: category.category_key,
  }));
}
