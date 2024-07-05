import CompareHeader from "@components/compare-header/CompareHeader";
import ComparingTargets from "@components/comparing-targets/ComparingTargets";
import ComparingData from "@components/comparing-data/ComparingData";

export default function CompareView() {
  return (
    <>
      <CompareHeader />
      <ComparingTargets />
      <ComparingData />
    </>
  );
}
