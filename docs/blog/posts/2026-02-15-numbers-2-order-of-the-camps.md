---
date: 2026-02-15
---

# Numbers 2

## The Order of the Camps

[Numbers 2 (BSB)](https://biblehub.com/bsb/numbers/2.htm)

<div id="sunburst-chart" style="height: 840px;"></div>
<script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
<script>
  const el = document.getElementById("sunburst-chart");
  const chart = echarts.init(el);
  chart.setOption({
    graphic: [
      {
        type: "circle",
        left: "center",
        top: "center",
        silent: true,
        zlevel: 10,
        z: 100,
        shape: { r: 58 },
        style: {
          fill: "#f8f1dc",
          stroke: "#8a6d1f",
          lineWidth: 2
        }
      },
      {
        type: "text",
        left: "center",
        top: "center",
        silent: true,
        zlevel: 11,
        z: 101,
        style: {
          text: "Tent of Meeting",
          fill: "#5a4713",
          font: "bold 12px sans-serif",
          align: "center",
          verticalAlign: "middle"
        }
      }
    ],
    series: {
      type: "sunburst",
      startAngle: 67.25,
      sort: null,
      data: [
        {
          name: "Levi",
          value: 603550,
          itemStyle: { color: "#d4af37" },
          children: [
            {
              name: "Judah",
              value: 186400,
              itemStyle: { color: "#40e0d0" },
              children: [
                { name: "Judah", value: 74600, itemStyle: { color: "#40e0d0" } },
                { name: "Issachar", value: 54400, itemStyle: { color: "#9966cc" } },
                { name: "Zebulun", value: 57400, itemStyle: { color: "#7fffd4" } }
              ]
            },
            {
              name: "Reuben",
              value: 151450,
              itemStyle: { color: "#e0115f" },
              children: [
                { name: "Reuben", value: 46500, itemStyle: { color: "#e0115f" } },
                { name: "Simeon", value: 59300, itemStyle: { color: "#ffc87c" } },
                { name: "Gad", value: 45650, itemStyle: { color: "#d73b3e" } }
              ]
            },
            {
              name: "Ephraim",
              value: 108100,
              itemStyle: { color: "#353839" },
              children: [
                { name: "Ephraim", value: 40500, itemStyle: { color: "#353839" } },
                { name: "Manasseh", value: 32200, itemStyle: { color: "#7a7d80" } },
                { name: "Benjamin", value: 35400, itemStyle: { color: "#c04000" } }
              ]
            },
            {
              name: "Dan",
              value: 157600,
              itemStyle: { color: "#0f52ba" },
              children: [
                { name: "Dan", value: 62700, itemStyle: { color: "#0f52ba" } },
                { name: "Asher", value: 41500, itemStyle: { color: "#9a7b4f" } },
                { name: "Naphtali", value: 53400, itemStyle: { color: "#eaf6ff" } }
              ]
            }
          ]
        }
      ]
    }
  });
</script>
