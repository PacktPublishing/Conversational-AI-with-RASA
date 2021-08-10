from rasa.shared.core.slots import Slot


class TableSlot(Slot):
    type_name = "table"

    def _feature_dimensionality(self):
        return 3

    def _as_feature(self):
        r = [0.0] * self._feature_dimensionality()
        if self.value:
            if self.value <= 4:
                r[0] = 1.0
            elif self.value <= 8:
                r[1] = 1.0
            else:
                r[2] = 1.0
        return r
