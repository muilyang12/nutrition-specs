import { foodApi } from "@apis/food";
import ClientCategoryMenu from "./CategoryMenu.client";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default async function CategoryMenu(props: Props) {
  const { selectedFoodCategoryKey } = props;

  const categories = await foodApi.getFoodCategories();

  if (!categories) return <></>;

  const parentsCategories = categories.filter((category) => !category.parent_category);

  return (
    <>
      <ClientCategoryMenu
        selectedFoodCategoryKey={selectedFoodCategoryKey}
        categories={parentsCategories}
      />
    </>
  );
}
