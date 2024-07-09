import LayoutHeader from "@components/layout-header/LayoutHeader";
import MainCategoryMenu from "@components/main-category-menu/MainCategoryMenu.server";
import ProductList from "@components/product-list/ProductList.server";

export default function HomeView() {
  return (
    <>
      <LayoutHeader />

      <MainCategoryMenu />

      <ProductList />
    </>
  );
}
