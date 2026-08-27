import unittest

from scripts.verify_profile import (
    public_github_metadata_issue,
    stale_profile_truth_issue,
)


class PublicGitHubBoundaryTests(unittest.TestCase):
    def test_public_safe_policy_passes(self) -> None:
        text = (
            "Live membership and repository access are owner-managed on GitHub "
            "and verified privately."
        )
        self.assertIsNone(public_github_metadata_issue(text))

    def test_exact_member_count_is_rejected(self) -> None:
        self.assertEqual(
            public_github_metadata_issue("The organization currently has 7 members."),
            "exact organization member count",
        )

    def test_written_member_count_is_rejected(self) -> None:
        self.assertEqual(
            public_github_metadata_issue("We are a team of seven members."),
            "exact organization member count",
        )

    def test_private_team_slug_is_rejected(self) -> None:
        self.assertEqual(
            public_github_metadata_issue("Assign the user to product-builders."),
            "exact private GitHub team slug",
        )

    def test_live_plan_is_rejected(self) -> None:
        self.assertEqual(
            public_github_metadata_issue("The studio currently uses GitHub Free."),
            "live organization plan",
        )

    def test_live_member_security_state_is_rejected(self) -> None:
        self.assertEqual(
            public_github_metadata_issue("All members have 2FA."),
            "live member security state",
        )

    def test_stale_svaeng_yul_truth_is_rejected(self) -> None:
        self.assertEqual(
            stale_profile_truth_issue("Khmer self-study video learning"),
            "obsolete Svaeng Yul tech-video framing",
        )

    def test_svaeng_yul_pilot_claim_is_rejected(self) -> None:
        text = (
            "| **Svaeng Yul** | Medical QCM practice. | "
            "Private class pilot. |"
        )
        self.assertEqual(
            stale_profile_truth_issue(text),
            "overstated Svaeng Yul pilot claim",
        )

    def test_unavailable_starter_adoption_claim_is_rejected(self) -> None:
        self.assertEqual(
            stale_profile_truth_issue(
                "Teams outside CHNAI LAB can adopt the AI-native team starter."
            ),
            "unavailable AI-native team starter adoption claim",
        )

    def test_fixed_product_count_is_rejected(self) -> None:
        for text in (
            "This applies to all seven product tracks.",
            "This is a seven-track intended portfolio.",
        ):
            with self.subTest(text=text):
                self.assertEqual(
                    stale_profile_truth_issue(text),
                    "fixed seven-product framing",
                )

    def test_overbroad_product_claims_are_rejected(self) -> None:
        cases = (
            ("Private core under hardening", "unverified Sat Digital core claim"),
            ("Trading software for signals", "overbroad Vantrex software claim"),
            ("SME operating system for shops", "overbroad PHSAROS operating-system claim"),
        )
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(stale_profile_truth_issue(text), expected)


if __name__ == "__main__":
    unittest.main()
