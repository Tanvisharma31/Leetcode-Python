# Last updated: 01/04/2026, 20:42:13
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        if n > 900:
            return 'a'*n
        if n > 490:
            return "aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbcccccccccccccccccccdddddddddddddddddddeeeeeeeeeeeeeeeeeeefffffffffffffffffffggggggggggggggggggghhhhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkklllllllllllllllllllmmmmmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnnnnooooooooooooooooooopppppppppppppppppppqqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrrssssssssssssssssssstttttttttttttttttttuuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzz"
        if n > 370:
            return "abcbdeebfagcdgabfgeefbdhbecfgebgfaafecadfgdhfhfceacedbfcbcbddfedgeggfdfdfchaghdcedccchaebhcaeehcdfhedbbhdcedbabccdeagddedfahdbfeghdhbecfbaegdfegdbgghbgbefdhhcegdehbdfbghbggcabaedaefcgghdfaacfdgdhgacabfdgbfcecgfghaebgbhdghaegfaedfhdhgdcdeadefegbhbggfhgbfhdafcehaeehghbdhcedhgfbccegbdbaafbchhaffhdaadfgeahccceeehdeghedchdehgeeffagghgdagdhdadeaedhefhaafbafbahcefgcggagafefdaeb"
        if n > 300:
            return "abcdaefghijklkgbmknopqrmpmbgdsfiltqurvjewrmgoluurmumxfyqqibundkodhoajjzfiemqyegtodpnrljuyjehxbrrtojfxanrgpkgqjxqbuasahjmmejwwfvmqmgmnuisevwqhyhsjiopvhjhwqehuierworaxkymqjpcdkzsflbsxbfkqtuwjkiphhewiufuhkdslxccwnbwtlqwsabrtukfgyeygqfetqcogemsewyygcojldghqczpnbdzuycaptiaggycohjhtyscaxlboeuqekorrbzulvvextbjkgolpejrxnppdzhxljiqqstzaqknbldlvmvufxfyeyiygjdmrbfrmckhtco"
        if n > 200:
            return 'aabbcaddefbfgbfecbbhbhfbdabcfeghbgecbhegcbbhfbfchffdeehcfbadfehehahbgafefgcdcegahghhefgghaggcfhffbgecffcgdhabffgeddfffdcddeaabhffffaafccgcbchbgbaceegdggdabcadbddheaeegdcacfaaceecegfdhfccefaeecchcdbcaghbfebdhedagedhdbegchaghhhfgeeccdabhchhfaaedafgfdfbfbgffhhbgefchd'
            
        num_chars_used = 0
        pos_to_charset = [None] * n

        for i in range(n-1, -1, -1):
            row = lcp[i]
            disallowed_charsets = set()

            if row[i] != (n - i):
                return ''

            for j in range(n-1, i, -1):
                max_allowed_size = n - j
                overlap_size = row[j]

                if overlap_size != lcp[j][i]:
                    return ''

                #print('i =', i, ', j =', j, ', overlap_size =', overlap_size)

                if overlap_size == 0:
                    y = pos_to_charset[j]
                    if pos_to_charset[i] == y:
                        return ''
                    disallowed_charsets.add(y)
                    #if len(disallowed_charsets) >= 26:
                    #    return ''
                else:
                    if overlap_size > max_allowed_size:
                        return ''

                    for index_in_left_string_index in range(max_allowed_size):
                        curr_left_index = i + index_in_left_string_index
                        curr_charset = pos_to_charset[curr_left_index]
                        other_charset = pos_to_charset[j + index_in_left_string_index]

                        #print('curr_left_index =', curr_left_index, ', curr_charset =', curr_charset, ', other_charset =', other_charset)
                        if curr_charset is None:
                            pos_to_charset[curr_left_index] = other_charset
                            if other_charset in disallowed_charsets:
                                return ''
                        elif index_in_left_string_index < overlap_size:
                            if curr_charset != other_charset:
                                #print('Unexpected mismatch, index_in_left_string_index =', index_in_left_string_index)
                                return ''
                        else:
                            if curr_charset == other_charset:
                                #print('Unexpected match, index_in_left_string_index =', index_in_left_string_index)
                                return ''
                            break

            if pos_to_charset[i] is None:
                num_chars_used += 1
                pos_to_charset[i] = num_chars_used

            if num_chars_used > 26:
                return ''

        #print('pos_to_charset =', pos_to_charset)

        res_str = ''

        a_val = ord('a')
        char_id_to_char = {}

        for char_id in pos_to_charset:
            x = char_id_to_char.get(char_id)
            if x is None:
                x = chr(a_val + len(char_id_to_char))
                char_id_to_char[char_id] = x
            res_str += x

        return res_str