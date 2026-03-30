Feature: Render Sentence

    Background:
        Given source documents in directory khm-sources

        Scenario Outline: Render Sentence Part
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the sentence part <sentence_part_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | sentence_part_id | output                                                                                                     |
                | 2    | 1       | 1      | s115             | -- "                                                                                                       |
                | 2    | 1       | 1      | s115_2           | Halbaus                                                                                                    |
                | 2    | 1       | 1      | s115_3           | " -- "Halbaus? was du sagst! den Namen habe ich gar noch nicht gehört, der steht gewiß nicht im Kalender." |
                | 53   | 1       | 1      | s8f4             | "Spieglein, Spieglein an der Wand:                                                                         |

        Scenario Outline: Render Sentence Part as XML ID
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            Given the sentece part renderer renders only the xmlid
            When I render the sentence part <sentence_part_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | sentence_part_id | output |
                | 2    | 1       | 1      | s115             | s115   |
                | 2    | 1       | 1      | s115_2           | s115_2 |
                | 2    | 1       | 1      | s115_3           | s115_3 |
                | 53   | 1       | 1      | s8f4             | s8f4   |

        Scenario Outline: Render Sentence
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            When I render the sentence <sentence_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | sentence_id        | output                                                                                                                |
                | 2    | 1       | 1      | s115-s115_2-s115_3 | -- "Halbaus" -- "Halbaus? was du sagst! den Namen habe ich gar noch nicht gehört, der steht gewiß nicht im Kalender." |
                | 53   | 1       | 1      | s8f4-s8f4_2        | "Spieglein, Spieglein an der Wand: wer ist die schönste Frau in dem ganzen Land?"                                     |
                # Inside line group inside paragraph
                | 11   | 1       | 1      | s215-s215_2        | was macht mein Reh? nun komme ich noch zweimal und dann nimmermehr."                                                  |
                # Inside line group outside paragraph
                | 30   | 1       | 1      | s531               | "was schreist du Flöhchen?" --                                                                                        |

        Scenario Outline: Render Sentence as XML IDs
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            Given the sentece part renderer renders only the xmlid
            When I render the sentence <sentence_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | sentence_id        | output           |
                # sentence split into parts because of rendition and no separators at rendition boundary
                | 2    | 1       | 1      | s115-s115_2-s115_3 | s115s115_2s115_3 |
                # Inside line group inside paragraph, sentence split into parts because it spans over multiple verse lines
                | 11   | 1       | 1      | s215-s215_2        | s215 s215_2      |
                | 53   | 1       | 1      | s8f4-s8f4_2        | s8f4 s8f4_2      |
                # Inside line group outside paragraph
                | 30   | 1       | 1      | s531               | s531             |

        Scenario Outline: Render Sentence With Custom Separators
            Given I parse the tale <tale> from edition <edition>, volume <volume>
            Given the word separator ¦
            When I render the sentence <sentence_id>
            Then the output is <output>

            Examples:
                | tale | edition | volume | sentence_id | output                                             |
                | 30   | 1       | 1      | s538        | Da¦fing¦der¦kleine¦Besen¦an¦entsetzlich¦zu¦kehren. |
