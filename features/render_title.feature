Feature: Render Title

    Background:
        Given source documents in directory khm-sources

        Scenario Outline: Render Title
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the head of the tale
            Then the output starts with <incipit>

            Examples:
                | tale | edition | volume | incipit                              |
                | 53   | 1       | 1      | 53. Schneewittchen (Schneeweißchen). |
                | 2    | 1       | 1      | 2. Katz und Maus in Gesellschaft.    |
                # Add more later when CI goes full live and we download all source files
