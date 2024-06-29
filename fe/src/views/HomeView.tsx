import FoodCategorySelect from "@components/FoodCategorySelect";
import ProductList from "@components/ProductList.server";

export default function HomeView() {
  return (
    <>
      <FoodCategorySelect />
      <ProductList />
    </>
  );
}
