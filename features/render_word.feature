Feature: Render Word

    Background:
        Given source documents in directory khm-sources

        Scenario Outline: Render Word Part
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the word part <word_part_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | word_part_id | output   |
                | 53   | 1       | 1      | wf9be        | Es       |
                | 53   | 1       | 1      | wf9bf        | war      |
                | 53   | 1       | 1      | wf9c0        | einmal   |
                | 53   | 1       | 1      | wf9c3        | Winter   |
                | 53   | 1       | 1      | wf9c4        | ,        |
                | 53   | 1       | 1      | wf9d1        | schöne   |
                | 53   | 1       | 1      | wf9dd        | Ebenholz |
                | 53   | 1       | 1      | wfa46        | .        |
                | 53   | 1       | 1      | wfa66        | "        |
                | 53   | 1       | 1      | w1043b       | toten    |
                | 53   | 1       | 1      | w1043b_1     |          |
                | 58   | 1       | 1      | w11bd7       | Mann     |

        Scenario Outline: Render Word
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the word <word_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | word_id         | output   |
                | 53   | 1       | 1      | wf9be           | Es       |
                | 53   | 1       | 1      | wfc50           | einander |
                | 53   | 1       | 1      | wfc50_1-wfc50_2 |          |
                | 53   | 1       | 1      | w1043b-w1043b_1 | toten    |
                | 58   | 1       | 1      | w11bd7          | Mann     |

        Scenario Outline: Render Word With Custom Separators
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            Given the word part separator •
            When I render the word <word_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | word_id         | output   |
                | 53   | 1       | 1      | wf9be           | Es       |
                | 53   | 1       | 1      | wfc50           | einander |
                | 53   | 1       | 1      | wfc50_1-wfc50_2 | •        |
                | 53   | 1       | 1      | w1043b-w1043b_1 | toten•   |
                | 58   | 1       | 1      | w11bd7          | Mann     |
