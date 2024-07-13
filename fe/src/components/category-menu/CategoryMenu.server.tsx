import { foodApi } from "@apis/food";
import MainCategoryMenu from "./MainCategoryMenu.client";
import SubCategoryMenu from "./SubCategoryMenu.client";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default async function CategoryMenu(props: Props) {
  const { selectedFoodCategoryKey } = props;

  const mainCategories = await foodApi.getMainFoodCategories();
  const currentCategory =
    selectedFoodCategoryKey &&
    (await foodApi.getFoodCategoryByCategoryKey(selectedFoodCategoryKey));

  if (!mainCategories) return <></>;

  let selectedMainCategoryKey: string | undefined;
  let selectedSubCategoryKey: string | undefined;

  if (!currentCategory) {
    selectedMainCategoryKey = undefined;
    selectedSubCategoryKey = undefined;
  } else if (!currentCategory.parent_category) {
    selectedMainCategoryKey = selectedFoodCategoryKey;
    selectedSubCategoryKey = undefined;
  } else {
    selectedMainCategoryKey = mainCategories.find(
      (category) => category.id === currentCategory.parent_category
    )?.category_key;
    selectedSubCategoryKey = selectedFoodCategoryKey;
  }

  const subCategories =
    selectedMainCategoryKey && (await foodApi.getSubFoodCategories(selectedMainCategoryKey));

  return (
    <>
      <MainCategoryMenu
        mainCategories={mainCategories}
        selectedMainCategoryKey={selectedMainCategoryKey}
      />
      {subCategories && (
        <SubCategoryMenu
          subCategories={subCategories}
          selectedSubCategoryKey={selectedSubCategoryKey}
        />
      )}
    </>
  );
}
