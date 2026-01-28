Feature: Render Title

    Background:
        Given source documents in directory khm-sources

        Scenario Outline: Render Number
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the number of the tale
            Then the output is <output>

            Examples:
                | tale | edition | volume | output |
                | 53   | 1       | 1      | 53     |
                | 2    | 1       | 1      | 2      |
                # Add more later when CI goes full live and we download all source files

        Scenario Outline: Render Title
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the title of the tale
            Then the output is <output>

            Examples:
                | tale | edition | volume | output                          |
                | 53   | 1       | 1      | Schneewittchen (Schneeweißchen) |
                | 2    | 1       | 1      | Katz und Maus in Gesellschaft   |
                # Add more later when CI goes full live and we download all source files

        Scenario Outline: Render Head
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the head of the tale
            Then the output is <output>

            Examples:
                | tale | edition | volume | output                              |
                | 53   | 1       | 1      | 53. Schneewittchen (Schneeweißchen) |
                | 2    | 1       | 1      | 2. Katz und Maus in Gesellschaft    |
                # Add more later when CI goes full live and we download all source files
