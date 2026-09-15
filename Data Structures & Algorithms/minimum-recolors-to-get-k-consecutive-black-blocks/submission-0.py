class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # k is either smaller or equal to block
        change = 0
        for index in range(k):
            if blocks[index] == 'W':
                change += 1
        # get the first block (if there is no other strign to parse, 
        # minim has already been minimised)
        minim = change

        for index in range(k, len(blocks)):
            if blocks[index] == 'B' and blocks[index - k + 1] == 'B':
                change -= 1
            elif blocks[index] == 'W' and blocks[index - k + 1] == 'B':
                change += 1
            minim = min(change, minim)


        return minim
            

        