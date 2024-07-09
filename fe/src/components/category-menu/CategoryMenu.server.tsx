import { foodApi } from "@apis/food";
import ClientCategoryMenu from "./CategoryMenu.client";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default async function CategoryMenu(props: Props) {
  const { selectedFoodCategoryKey } = props;

  const mainCategories = await foodApi.getMainFoodCategories();

  if (!mainCategories) return <></>;

  return (
    <>
      <ClientCategoryMenu
        selectedFoodCategoryKey={selectedFoodCategoryKey}
        mainCategories={mainCategories}
      />
    </>
  );
}
