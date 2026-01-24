Feature: Render Title

    Background:
        Given source documents in directory khm-sources

        Scenario Outline: Tale From Correct File
            When I render the title of the tale <tale> from edition <edition>, volume <volume>
            Then the output starts with <incipit>

            Examples:
                | tale | edition | volume | incipit                              |
                | 53   | 1       | 1      | 53. Schneewittchen (Schneeweißchen). |
                | 2    | 1       | 1      | 2. Katz und Maus in Gesellschaft.    |
