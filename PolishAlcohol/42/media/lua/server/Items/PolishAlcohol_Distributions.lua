require "Items/ProceduralDistributions"

-- Append to vanilla lists, rather than replacing them. Weights are relative loot
-- weights, not percentages. Missing lists are skipped on different 42 builds.
local additions = {
    LiquorStoreBeerFancy = { "Zywiec", "Tyskie", "Lech", "Zubr", "Kustosz", "Romper", "Imperator", "Karpackie", "Tatra", "Harnas" },
    LiquorStoreBeer = { "Zywiec", "Tyskie", "Lech", "Zubr", "Kustosz", "Romper", "Imperator", "Karpackie", "Tatra", "Harnas" },
    LiquorStoreWhiskey = { "Zubrowka", "Wyborowa", "Soplica", "AdamMickiewicz", "Chopin", "Wratislavia" },
    LiquorStoreLiquor = { "Zubrowka", "Wyborowa", "Soplica", "AdamMickiewicz", "Chopin", "Wratislavia" },
    BarShelfLiquor = { "Zubrowka", "Wyborowa", "Soplica", "AdamMickiewicz", "Chopin", "Wratislavia" },
    BarCounterLiquor = { "Zubrowka", "Wyborowa", "Soplica", "AdamMickiewicz", "Chopin", "Wratislavia" },
    FridgeBeer = { "Zywiec", "Tyskie", "Lech", "Zubr", "Kustosz", "Romper", "Imperator", "Karpackie", "Tatra", "Harnas" },
    StoreShelfBeer = { "Zywiec", "Tyskie", "Lech", "Zubr", "Kustosz", "Romper", "Imperator", "Karpackie", "Tatra", "Harnas" },
    BarShelfBeer = { "Zywiec", "Tyskie", "Lech", "Zubr", "Kustosz", "Romper", "Imperator", "Karpackie", "Tatra", "Harnas" },
    FridgeSoda = { "Zywiec", "Tyskie", "Lech", "Zubr", "Kustosz", "Romper", "Imperator", "Karpackie", "Tatra", "Harnas" },
    GigamartBottles = { "Zywiec", "Tyskie", "Lech", "Zubr", "Kustosz", "Romper", "Imperator", "Karpackie", "Tatra", "Harnas", "Zubrowka", "Wyborowa", "Soplica", "AdamMickiewicz", "Chopin", "Wratislavia" },
}

for name, drinks in pairs(additions) do
    local distribution = ProceduralDistributions.list[name]
    if distribution and distribution.items then
        for _, drink in ipairs(drinks) do
            table.insert(distribution.items, "Base.Polish" .. drink)
            table.insert(distribution.items, 2)
        end
    end
end
