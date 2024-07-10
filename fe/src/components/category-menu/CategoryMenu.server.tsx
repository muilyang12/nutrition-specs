import { foodApi } from "@apis/food";
import MainCategoryMenu from "./MainCategoryMenu.client";
import SubCategoryMenu from "./SubCategoryMenu.client";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default async function CategoryMenu(props: Props) {
  const { selectedFoodCategoryKey } = props;

  if (!selectedFoodCategoryKey) return <></>;

  const mainCategories = await foodApi.getMainFoodCategories();
  const currentCategory = await foodApi.getFoodCategoryByCategoryKey(selectedFoodCategoryKey);

  if (!mainCategories || !currentCategory) return <></>;

  let selectedMainCategoryKey: string | undefined;
  let selectedSubCategoryKey: string | undefined;

  if (!currentCategory.parent_category) {
    selectedMainCategoryKey = selectedFoodCategoryKey;
    selectedSubCategoryKey = undefined;
  } else {
    selectedMainCategoryKey = mainCategories.find(
      (category) => category.id === currentCategory.parent_category
    )?.category_key;
    selectedSubCategoryKey = selectedFoodCategoryKey;
  }

  if (!selectedMainCategoryKey) return <></>;

  const subCategories = await foodApi.getSubFoodCategories(selectedMainCategoryKey);

  return (
    <>
      <MainCategoryMenu
        mainCategories={mainCategories}
        selectedMainCategoryKey={selectedMainCategoryKey}
      />
      <SubCategoryMenu
        subCategories={subCategories}
        selectedSubCategoryKey={selectedSubCategoryKey}
      />
    </>
  );
}
