# coding=utf-8


class BinHeap(object):
    def __init__(self, items=()):
        self._list = []
        for item in items:
            self.push(item)

    def push(self, val):
        pos = len(self._list)  # Note: getting length before add
        self._list.append(val)

        # Compares the a value in the list with its parent and swaps if value is greater
        while pos > 0:
            parent_index = (pos - 1) // 2
            if val > self._list[parent_index]:
                self._list[pos] = self._list[parent_index]
                pos = parent_index
            else:
                break

        # If we get here we're at the top of the list or found where to put the value
        self._list[pos] = val

    def pop(self):
        return_value = self._list[0]
        val = self._list.pop()
        if self._list:
            pos = 0
            while True:
                left = pos * 2 + 1
                right = left + 1

                # checks if we have a left
                if left >= len(self._list):
                    break

                # if left is the bigger/only child
                if right >= len(self._list) or self._list[left] > self._list[right]:
                    bigger_child = left
                else:
                    bigger_child = right

                # Check and/or swap with the bigger child
                if self._list[bigger_child] > val:
                    self._list[pos] = self._list[bigger_child]
                    pos = bigger_child
                else:
                    # If we reach here we are bigger than our children and are done
                    break

            # If we get here we're at the bottom of the list or found where to put the value
            self._list[pos] = val

        return return_value
