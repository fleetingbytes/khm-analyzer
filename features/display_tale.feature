Feature: Dislpay Tale

    Rule: Tale is from the specified source file
        Background:
            Given source documents in directory khm-sources

        Scenario Outline:
            When I display the tale <tale> from edition <edition>, volume <volume>
            Then the output starts with <incipit>

            Examples:
                | tale | edition | volume | incipit                        |
                | 53   | 1       | 1      | Es war einmal mitten im Winter |
