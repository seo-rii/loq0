ACTION_MOVE = 0
ACTION_PLACE_I = 1
ACTION_PLACE_L = 2


def act(self, t, p1, p2, p3):
    if t == ACTION_MOVE:
        return self.move(p1, p2)
    if t == ACTION_PLACE_I:
        return self.place_i(p1, p2, p3)
    if t == ACTION_PLACE_L:
        return self.place_l(p1, p2, p3)
    return False
