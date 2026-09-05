Feature: Document Structure

    Background:
        Given source documents in directory khm-sources

        @wip
        Scenario Outline: Number of Tales in Each Document
            Given I parse all tales in edition <edition>, volume <volume>
            When I render the numbers of all the tales
            Then the output is <output>

            Examples:
                | edition | volume | output                                                                                                                                                                                                                                                   |
                | 1       | 1      | 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 30 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 |

# Number of Subtales in Tale ...
# Number of Sentences in Tale ...
# Number of Line Groups in Tale ...
# Zero Lines which are outside of line group
# Number of direct Children in Tale ...
