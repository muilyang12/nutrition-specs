import { Suspense } from "react";
import LayoutHeader from "@components/layout-header/LayoutHeader";
import ComparingTargets from "@components/comparing-targets/ComparingTargets";
import ComparingData from "@components/comparing-data/ComparingData";

export default function CompareView() {
  return (
    <>
      <LayoutHeader />

      <Suspense>
        <ComparingTargets />
      </Suspense>

      <Suspense>
        <ComparingData />
      </Suspense>
    </>
  );
}
