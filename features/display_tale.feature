Feature: Dislpay Tale

    Background:
        Given source documents in directory khm-sources

    Rule: Tale is from the specified source file

        Scenario Outline: Tale From Correct File
            When I display the tale <tale> from edition <edition>, volume <volume>
            Then the output starts with <incipit>

            Examples:
                | tale | edition | volume | incipit                        |
                | 53   | 1       | 1      | Es war einmal mitten im Winter |
                # Add more later when CI goes full live and we download all source files

    Rule: Optionally display tale metadata

        Scenario Outline: Tale number
            When I select the option to show the tale number
            When I display the tale <tale> from edition <edition>, volume <volume>
            Then the output starts with <incipit>

            Examples:
                | tale | edition | volume | incipit |
                | 53   | 1       | 1      | 53.     |

        Scenario Outline: Tale Title
            When I select the option to show the tale title
            When I display the tale <tale> from edition <edition>, volume <volume>
            Then the output starts with <incipit>

            Examples:
                | tale | edition | volume | incipit      |
                | 53   | 1       | 1      | Schneewittchen |


        Scenario Outline: Tale Number and Title
            When I select the option to show the tale number
            When I select the option to show the tale title
            When I display the tale <tale> from edition <edition>, volume <volume>
            Then the output starts with <incipit>

            Examples:
                | tale | edition | volume | incipit          |
                | 53   | 1       | 1      | 53. Schneewittchen |

