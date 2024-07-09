import { foodApi } from "@apis/food";
import ClientMainCategoryMenu from "./MainCategoryMenu.client";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default async function MainCategoryMenu(props: Props) {
  const { selectedFoodCategoryKey } = props;

  const mainCategories = await foodApi.getMainFoodCategories();

  if (!mainCategories) return <></>;

  return (
    <>
      <ClientMainCategoryMenu
        selectedFoodCategoryKey={selectedFoodCategoryKey}
        mainCategories={mainCategories}
      />
    </>
  );
}
