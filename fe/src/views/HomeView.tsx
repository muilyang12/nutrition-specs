import LayoutHeader from "@components/layout-header/LayoutHeader";
import CategoryMenu from "@components/category-menu/CategoryMenu.server";
import ProductList from "@components/product-list/ProductList.server";

export default function HomeView() {
  return (
    <>
      <header>
        <LayoutHeader />

        <CategoryMenu />
      </header>
    </>
  );
}
