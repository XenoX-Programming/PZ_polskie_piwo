require "Items/ProceduralDistributions"

-- Append to vanilla lists, rather than replacing them. Weights are relative loot
-- weights, not percentages. Missing lists are skipped on different 42 builds.
local additions = {
    LiquorStoreBeerFancy = { "Zywiec", "Tyskie", "Lech", "Zubr" },
    LiquorStoreBeer = { "Zywiec", "Tyskie", "Lech", "Zubr" },
    LiquorStoreWhiskey = { "Zubrowka", "Wyborowa", "Soplica" },
    LiquorStoreLiquor = { "Zubrowka", "Wyborowa", "Soplica" },
    BarShelfLiquor = { "Zubrowka", "Wyborowa", "Soplica" },
    BarCounterLiquor = { "Zubrowka", "Wyborowa", "Soplica" },
    FridgeBeer = { "Zywiec", "Tyskie", "Lech", "Zubr" },
    StoreShelfBeer = { "Zywiec", "Tyskie", "Lech", "Zubr" },
    BarShelfBeer = { "Zywiec", "Tyskie", "Lech", "Zubr" },
    FridgeSoda = { "Zywiec", "Tyskie", "Lech", "Zubr" },
    GigamartBottles = { "Zywiec", "Tyskie", "Lech", "Zubr", "Zubrowka", "Wyborowa", "Soplica" },
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
