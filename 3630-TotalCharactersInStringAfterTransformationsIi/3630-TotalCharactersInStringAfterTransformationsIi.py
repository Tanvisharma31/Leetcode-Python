# Last updated: 02/03/2026, 13:56:36
import numpy as np

MOD = 10**9 + 7

# NOTE: most of this logic was stolen from my Rabin-Karp numpy implementation

# NOTE: don't do np.uint64 (matrix entries COULD be negative)
# ^ UPD: well actually, since everything is under MOD, you could just begin by MODDING every entry to make them non-negative...
INT_TYPE = np.int64
MAX_VAL = 2**63-1
MAX_VAL_MSB = 63
MAX_MODDED_VAL = MOD-1
MAX_MODDED_VAL_MSB = (MOD-1).bit_length()
MAX_MODDED_SHIFT = MAX_VAL_MSB - MAX_MODDED_VAL_MSB

# MSB == number of bits to represent the value
HALF_MASK_MSB = int(ceil(MAX_MODDED_VAL_MSB / 2))
HALF_MASK = INT_TYPE((1<<HALF_MASK_MSB) - 1)
# HALF_HALF_PRODUCT_MSB = 2 * HALF_MASK_MSB

THIRD_MASK_MSB = int(ceil(MAX_MODDED_VAL_MSB / 3))
THIRD_MASK = INT_TYPE((1<<THIRD_MASK_MSB) - 1)


# check that we have some margin to add together a few modded values w/o worrying about overflow
MARGIN_MSB = 60
assert(MAX_MODDED_VAL_MSB <= MARGIN_MSB)


# initial_shift_sz == amount that caller guarantees that you can shift initial input w/o overflow
# shift_sz == amount that you can shift an arbitrary modded value (worst case MOD-1) w/o overflow
# TODO: remove the shift_sz argument, since it is globally fixed
def _modular_lshift(arr, rem, shift_sz, initial_shift_sz):
    # total_modulo_count = 0

    # initial shift
    if initial_shift_sz:
        sh = min(rem, initial_shift_sz)
        arr <<= sh
        rem -= sh
    
    arr %= MOD
    # total_modulo_count += 1
    
    # subsequent shifts
    while rem:
        sh = min(rem, shift_sz)
        arr <<= sh
        arr %= MOD
        # total_modulo_count += 1
        rem -= sh
    
    # print(f"total number of modulos for this modular lshift = {total_modulo_count}")
    return arr

# NOTE: instead of multiplying pairwise elements a[i]/b[i],
# we are now going to multiply two matrices,
# (which values are all initially < MOD)

# NOTE: number of x*y elements that we sum together ==
# num_cols in a (aka. num_rows in b)
# ^ this affects the INITIAL_SHIFT that we feed into _modular_lshift

def mat_mod_mul(a, b):
    d = len(b)
    ADDITION_MSB = d.bit_length()

    '''
    print(a)
    for row in a:
        print(row)
        for x in row:
            print(x)
            assert(x <= MAX_MODDED_VAL)
    for row in b:
        for x in row:
            assert(x <= MAX_MODDED_VAL)
    '''
    # assert(np.all(a <= MAX_MODDED_VAL))
    # assert(np.all(b <= MAX_MODDED_VAL))

    
    if (MAX_MODDED_VAL**2) * d <= MAX_VAL:
        return a @ b % MOD
    # a, b -> a, bL/bH
    
    # elif MAX_MODDED_VAL_MSB + HALF_MASK_MSB + ADDITION_MSB <= MARGIN_MSB:
    if True: # DEBUG
        MAX_PRODUCT_INITIAL_MSB = MAX_MODDED_VAL_MSB + HALF_MASK_MSB + ADDITION_MSB 
        MAX_PRODUCT_INITIAL_SHIFT = MAX_VAL_MSB - MAX_PRODUCT_INITIAL_MSB

        bL = b & HALF_MASK
        bH = b >> HALF_MASK_MSB

        L = a @ bL
        H = a @ bH

        Hsh = _modular_lshift(H, HALF_MASK_MSB, MAX_MODDED_SHIFT, MAX_PRODUCT_INITIAL_SHIFT)

        return (Hsh + L) % MOD
    # a, b -> a, bL/bM/bH
    elif MAX_MODDED_VAL_MSB + THIRD_MASK_MSB + ADDITION_MSB <= MARGIN_MSB:
    # if True: # DEBUG
        MAX_PRODUCT_INITIAL_MSB = MAX_MODDED_VAL_MSB + THIRD_MASK_MSB + ADDITION_MSB
        MAX_PRODUCT_INITIAL_SHIFT = MAX_VAL_MSB - MAX_PRODUCT_INITIAL_MSB

        bL = b & THIRD_MASK
        bM = (b >> THIRD_MASK_MSB) & THIRD_MASK
        bH = b >> (2*THIRD_MASK_MSB)

        L = a @ bL
        M = a @ bM
        H = a @ bH

        Hsh = _modular_lshift(H, THIRD_MASK_MSB, MAX_MODDED_SHIFT, MAX_PRODUCT_INITIAL_SHIFT)
        M_Hsh = M + Hsh
        M_Hsh_sh = _modular_lshift(M_Hsh, THIRD_MASK_MSB, MAX_MODDED_SHIFT, MAX_PRODUCT_INITIAL_SHIFT - 1)

        return (L + M_Hsh_sh) % MOD
    # a, b -> aL/aH, bL/bH
    else:
        # MAX_PRODUCT_INITIAL_MSB = HALF_HALF_PRODUCT_MSB + ADDITION_MSB
        MAX_PRODUCT_INITIAL_MSB = 2*HALF_MASK_MSB + ADDITION_MSB
        MAX_PRODUCT_INITIAL_SHIFT = MAX_VAL_MSB - MAX_PRODUCT_INITIAL_MSB

        aL = a & HALF_MASK
        aH = a >> HALF_MASK_MSB
        bL = b & HALF_MASK
        bH = b >> HALF_MASK_MSB

        LL = aL @ bL
        LH = aL @ bH
        HL = aH @ bL
        HH = aH @ bH

        HHsh = _modular_lshift(HH, HALF_MASK_MSB, MAX_MODDED_SHIFT, MAX_PRODUCT_INITIAL_SHIFT)

        # adding together 1 value of MAX_MODDED_VAL_MSB + 2 values of 2*HALF_MASK_MSB
        LH_HL_HHsh = HHsh + HL + LH
        LH_HL_HHsh_sh = _modular_lshift(LH_HL_HHsh, HALF_MASK_MSB, MAX_MODDED_SHIFT, MAX_PRODUCT_INITIAL_SHIFT - 2)

        return (LL + LH_HL_HHsh_sh) % MOD


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, send: List[int]) -> int:


        freq = list(map(Counter(s).__getitem__, ascii_lowercase))
        # vector to be multiplied
        freq_list_vector = [[x] for x in freq]
        freq_vector = np.matrix(freq, dtype=INT_TYPE).T

        a = [[0]*26 for _ in range(26)]

        for c in range(26):
            for shift in range(1, send[c] + 1):
                C = (c + shift) % 26
                # [to][from]
                a[C][c] = 1
        
        '''
        # TODO: heuristic optimization == don't even add anything if one of the two input cells is 0
        # there might be a considerable amount of sparseness
        # doesn't cost much to check if either of them are 0

        def mat_mul(a, b):
            h,w,d = len(a), len(b[0]), len(b)

            ret = [[0]*w for _ in range(h)]
            for i in range(h):
                for j in range(w):
                    for k in range(d):
                        ret[i][j] += a[i][k] * b[k][j]
                    ret[i][j] %= MOD
            return ret

        def mat_exp(mat, rem):
            if rem == 1:
                return mat
            elif rem % 2:
                return mat_mul(mat, mat_exp(mat, rem-1))
            else: # rem is even
                subret = mat_exp(mat, rem // 2)
                return mat_mul(subret, subret)
        
        return sum(chain.from_iterable(mat_mul(mat_exp(a, t), freq_list_vector))) % MOD
        '''

        mat = np.matrix(a, dtype=INT_TYPE)

        def bin_exp(matrix, rem):
            if rem == 1:
                return mat
            elif rem % 2:
                return mat_mod_mul(mat, bin_exp(mat, rem-1))
            else:
                subret = bin_exp(mat, rem // 2)
                return mat_mod_mul(subret, subret)
                # return subret @ subret % MOD
                # return (bin_exp(mat, rem // 2) ** 2) % MOD
        
        mat_pow = bin_exp(mat, t)
        ret_vector = mat_mod_mul(mat_pow, freq_vector)
        return int(np.sum(ret_vector)) % MOD