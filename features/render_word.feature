Feature: Render Word

    Background:
        Given source documents in directory khm-sources

        Scenario Outline: Render Word Part
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the word part <word_part_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | word_part_id | output |
                | 53   | 1       | 1      | w1043b       | toten  |
                | 53   | 1       | 1      | w1043b_1     |        |

        @debug
        Scenario Outline: Render Word
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the word <word_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | word_id         | output |
                | 53   | 1       | 1      | w1043b-w1043b_1 | toten  |
